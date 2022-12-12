var data = null;
function requestData()
{
  $.ajax({
    url: "/sensor-data",
    type : 'GET',
    success: function(html)
    {
      var data = html[1];

      Highcharts.chart('container', {
        title: {
          text: 'Temp'
        },
        yAxis: {
          title: {
            text: 'Temp'
          }
        },
        xAxis: {
          title:{
            text:'count'
          }
        },
        legend: {
          layout: 'vertical',
          align: 'right',
          verticalAlign: 'middle'
        },
        plotOptions: {
          series: {
            label: {
              connectorAllowed: false
            },
            pointStart: 1
          }
        },
        series: [{
          name: 'Temp',
          data: data
        },
        ],
        responsive: {
          rules: [{
            condition: {
              maxWidth: 500
            },
            chartOptions: {
              legend: {
                layout: 'horizontal',
                align: 'center',
                verticalAlign: 'bottom'
              }
            }
          }]
        }
      })
    },
    cache:false
  });
}
$(document).ready(function() {
    requestData();
    setInterval(requestData,30000);
  });