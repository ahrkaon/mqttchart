function requestData() {
    $.ajax({
        url: '/sensor-data',
        success: function(point) {
            setInterval(requestData, 1000)
        },
        cache: false
    });
}

const ctx = document.getElementById('myChart');

new Chart(ctx, {
  type: 'line',
  data: {
    labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
    datasets: [{
      label: '# of Votes',
      data: [12, 19, 3, 5, 2, 3],
      borderWidth: 0,
      fill: false
    }]
  },
  options: {
    scales: {
      y: {
        beginAtZero: false
      }
    }
  }
});