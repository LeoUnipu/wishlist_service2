document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById('itemForm');
    form.addEventListener('submit', function (event) {
        const naziv = document.getElementById('naziv').value;
        const cijena = document.getElementById('cijena').value;

        if (!naziv || !cijena) {
            alert("Sva polja moraju biti popunjena!");
            event.preventDefault();  
        }
    });
});