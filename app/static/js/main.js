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

function addSongToPlaylistDiv(title, artist, song_id) {
    var songHTML = `<div class="song-container" id="${song_id}"> 
                        <div class="start-song-div">  
                                <p class="start-song-section"><b>${title}</b>- ${artist}</p> 
                        </div> 
                        <div class="middle-song-div"> 
                            <p class="middle-song-section">34.002</p> 
                        </div> 
                        <div class="end-song-div"> 
                            <button class="end-song-section add-song-button" value="${song_id}" onclick="removeSong(this.value)">-</button> 
                        </div> 
                    </div>`;
    document.getElementById("playlist-div-id").innerHTML += songHTML;
}

function addSongToSuggestionDiv(title, artist, song_id) {
    var songHTML = `<div class="song-container" id="${song_id}">
                        <div class="start-song-div">
                            <p class="start-song-section"><b>${title} </b> - ${artist}</p>
                        </div>
                        <div class="middle-song-div">
                            <p class="middle-song-section">placholder</p>
                        </div>
                        <div class="end-song-div"><button class="end-song-section add-song-button" value="${song_id}" onclick="addSong(value)">+</button></div>
                    </div>`
    document.getElementById("suggestion-container-songs").innerHTML += songHTML;
}

function suggestSongs() {
    // clear inside div 
    document.getElementById("suggestion-container-songs").innerHTML = "";


    fetch('/playerlist_suggestions', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                status: 200
            })
        })
        .then(response => response.json())
        .then(data => {

            songs_data = data.data;

            for (let i = 0; i < songs_data.length; i++) {
                addSongToSuggestionDiv(songs_data[i].track_name, songs_data[i].track_artist, songs_data[i].track_id);
            }
        });
}


// behind the button of the suggested songs
function addSong(id) {
    addSongFromId(id);
    removeElementById(id);
}

function addSongFromInput() {
    // gettting the id - not nice
    var strInput = document.getElementById("search-input").value;
    console.log(strInput);
    var song_id = strInput.slice(-36);

    addSongFromId(song_id);
    document.getElementById("search-input").value = "";
}

function addSongFromId(song_id) {
    // adding the entry to the playlist div and the list in python api 

    fetch('/add_song_to_playlist', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                song_id: song_id
            })
        })
        .then(response => response.json())
        .then(data => {
            track_name = data.track_name;
            track_artist = data.track_artist;
            track_id = data.track_id;
            addSongToPlaylistDiv(track_name, track_artist, track_id);
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
            removeElementById(the_song_id);
        });
}

// util
function removeElementById(song_id) {
    document.getElementById(song_id).remove();
}