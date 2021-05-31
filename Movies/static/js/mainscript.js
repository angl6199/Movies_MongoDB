disableSearch()

document.getElementById('search-fields').onclick = function(){
    if (document.getElementById('search-fields').value == "Choose one..."){
            disableSearch()
        }
    else {
            enableSearch()
    }
}

document.getElementById('all-movies').onclick = function(){
    window.alert("Please consider that all data inside table movies will take a few seconds to render due to its length.")
}

function disableSearch() {
    document.getElementById('search-but').disabled = true;
    document.getElementById('search-but').style.backgroundColor = 'grey';
    document.getElementById('search-input').disabled = true;
    document.getElementById('search-input').style.backgroundColor = 'rgba(128, 128, 128, 0.15)';
    document.getElementById('search-input').placeholder = "Select a valid field...";
}

function enableSearch() {
    document.getElementById('search-but').disabled = false;
    document.getElementById('search-but').style.backgroundColor = 'var(--secondary)';
    document.getElementById('search-input').disabled = false;
    document.getElementById('search-input').style.backgroundColor = 'rgba(229, 9, 20, 0.05)';
    document.getElementById('search-input').placeholder = "Search...";
}