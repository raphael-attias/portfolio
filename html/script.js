window.onload = function () {
    const letterR = document.getElementById('R');
    const letterA = document.getElementById('A');
    const nameContainer = document.getElementById('name');

    // Lancer l'animation des lettres
    letterR.classList.add('animate');
    letterA.classList.add('animate');

    // Attendre la fin de l'animation des lettres
    setTimeout(() => {
        // Afficher le nom "Raphaël ATTIAS" après 2s (durée des animations)
        nameContainer.classList.remove('hidden');
        nameContainer.classList.add('visible');
    }, 750); // 2s pour correspondre aux animations exactes
};

window.onscroll = function () {
    const scrollPosition = window.scrollY || document.documentElement.scrollTop;

    if (scrollPosition > 200) {
        document.body.classList.add('scroll-triggered');
    } else {
        document.body.classList.remove('scroll-triggered');
    }
};
