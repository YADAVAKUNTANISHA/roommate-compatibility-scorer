function calculateCompatibility() {
    // Collect the user inputs and calculate compatibility logic
    var score = 0;

    // Sleep Time Compatibility
    if (document.getElementById('sleep1').value === document.getElementById('sleep2').value) {
        score += 10;
    }

    // Cleanliness Compatibility
    if (document.getElementById('cleanliness1').value === document.getElementById('cleanliness2').value) {
        score += 20;
    }

    // Work Schedule Compatibility
    if (document.getElementById('workSchedule1').value === document.getElementById('workSchedule2').value) {
        score += 30;
    }

    // Food Habits Compatibility
    if (document.getElementById('foodHabits1').value === document.getElementById('foodHabits2').value) {
        score += 40;
    }

    document.getElementById('score').innerText = score;
}
