function deleteNote(noteId) {
    fetch("/delete-note", {
        method: "POST",
        body: JSON.stringify({ noteId: noteId }), // turn it into string 
    }).then((_res) => {
        // return to url / which means home page 
        window.location.href = "/"; 
    });
}

/*************** custome *************/
const listContainer = document.getElementById("notes");
 
listContainer.addEventListener("click", function(e) {
    if(e.target.tagName === "LI") {
        e.target.classList.toggle("checked");
    }
    else if(e.target.tagName === "SPAN") {
        e.target.parentElement.remove();
    }
}, false); 
 

