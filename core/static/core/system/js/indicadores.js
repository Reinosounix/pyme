$(document).ready(function(){       
    $.getJSON('https://mindicador.cl/api', function(data) {
        var dailyIndicators = data;
        var uf = Math.round(dailyIndicators.uf.valor);
        var dolar = Math.round(dailyIndicators.dolar.valor);
        $("#value_uf").val(uf); 
        $("#value_dolar").val(dolar); 
    }).fail(function() {
        console.log('Error al consumir la API!');
    });
});
