$(document).ready(function(){
    $('#like1').click(function () {
        id = $(this).attr('data-item');
        $('#inputlike').val(id);
        $(".like1").removeClass('yes1');
        $('#em').text('Ужасно')
        $('#like1').addClass('yes1');
    });
    $('#like2').click(function () {
        $(".like1").removeClass('yes1');
        $('#em').text('Плохо')
        $('#like1, #like2').addClass('yes1');
        id = $(this).attr('data-item');
        $('#inputlike').val(id);
    });
    $('#like3').click(function () {
        $(".like1").removeClass('yes1');
        $('#em').text('Неплохо')
        $('#like1, #like2, #like3').addClass('yes1');
        id = $(this).attr('data-item');
        $('#inputlike').val(id);
    });
    $('#like4').click(function () {
        $(".like1").removeClass('yes1');
        $('#em').text('Хорошо')
        $('#like1, #like2, #like3, #like4').addClass('yes1');
        id = $(this).attr('data-item');
        $('#inputlike').val(id);
    });
    $('#like5').click(function () {
        $(".like1").removeClass('yes1');
        $('#em').text('Отлично')
        $('#like1, #like2, #like3, #like4, #like5').addClass('yes1');
        id = $(this).attr('data-item');
        $('#inputlike').val(id);
    });
    $("#like1").mouseover(function() { $('#like1').addClass("yes"); $('#em').text('Ужасно') });
    $("#like2").mouseover(function() { $('#like1, #like2').addClass("yes"); $('#em').text('Плохо')});
    $("#like3").mouseover(function() { $('#like1, #like2, #like3').addClass("yes");$('#em').text('Неплохо') });
    $("#like4").mouseover(function() { $('#like1, #like2, #like3, #like4').addClass("yes"); $('#em').text('Хорошо')});
    $("#like5").mouseover(function() { $('#like1, #like2, #like3, #like4, #like5').addClass("yes");$('#em').text('Отлично') });
    $("#like1, #like2, #like3, #like4, #like5").mouseout(function() { $('#like1, #like2, #like3, #like4, #like5').removeClass("yes"); $('#em').text('Нажмите, чтобы оценить') });
    

});
