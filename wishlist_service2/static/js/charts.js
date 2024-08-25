document.addEventListener('DOMContentLoaded', function() {
    const ctx = document.getElementById('statsChart').getContext('2d');

    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['Ukupno stavki', 'Kupljeni predmeti', 'Ukupno potrošeno'],
            datasets: [{
                label: 'Statistika popisa želja',
                data: [
                    window.statsData.totalItems,
                    window.statsData.boughtItems,
                    window.statsData.totalSpent
                ],
                backgroundColor: [
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)'
                ],
                borderColor: [
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    type: 'logarithmic',
                    beginAtZero: true
                }
            }
        }
    });
});






