// song suggestions
function sendInput(input_data) {
    fetch('/word_search', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                input: input_data
            })
        })
        .then(response => response.json())
        .then(data => {
            // clearing datalist
            const datalist = document.getElementById("song-suggestions");
            while (datalist.firstChild) {
                datalist.removeChild(datalist.firstChild);
            }

            json_array_songs = data.data;
            json_array_songs.forEach(element => {
                const option = document.createElement('option');
                option.value = element.track_name + " " + element.track_id;
                datalist.appendChild(option);
            });
        });
}

document.getElementById('search-input').addEventListener('input', function(event) {
    sendInput(event.target.value);
});

// add song to playlist visually
function addSong(title, artist, song_id) {
    var songHTML = `<div class="song-container" id="${song_id}"> <div class="start-song-div">  <p class="start-song-section"><b>${title}</b>- ${artist}</p> </div> <div class="middle-song-div"> <p class="middle-song-section">34.002</p> </div> <div class="end-song-div"> <button class="end-song-section add-song-button" value="${song_id}" onclick="removeSong(this.value)">-</button> </div> </div>`;
    document.getElementById("playlist-div-id").innerHTML += songHTML;
}

function removeSongFromDiv(song_id) {
    document.getElementById(song_id).remove();
}

function addSongFromInput() {
    var strInput = document.getElementById("search-input").value;
    console.log(strInput);
    var the_song_id = strInput.slice(-36);

    // adding the entry to the playlist div and the list in python api 
    fetch('/add_song_to_playlist', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                song_id: the_song_id
            })
        })
        .then(response => response.json())
        .then(data => {
            track_name = data.track_name;
            track_artist = data.track_artist;
            track_id = data.track_id;
            // adding song to playlist div
            addSong(track_name, track_artist, track_id);
        });

}

function removeSong(the_song_id) {
    fetch('/remove_song', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                song_id: the_song_id
            })
        })
        .then(response => response.json())
        .then(data => {
            // remove the song from the ui
            removeSongFromDiv(the_song_id);
        });

}