$.ajaxSetup({ 
     beforeSend: function(xhr, settings) {
         function getCookie(name) {
             var cookieValue = null;
             if (document.cookie && document.cookie != '') {
                 var cookies = document.cookie.split(';');
                 for (var i = 0; i < cookies.length; i++) {
                     var cookie = jQuery.trim(cookies[i]);
                     // Does this cookie string begin with the name we want?
                     if (cookie.substring(0, name.length + 1) == (name + '=')) {
                         cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                         break;
                     }
                 }
             }
             return cookieValue;
         }
         if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
             // Only send the token to relative URLs i.e. locally.
             xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
         }
     } 
});

$(document).ready(function(){
    var now = $('#datepicker').val()
    datepicker = $('#datepicker').datepicker(
        {
            dateFormat: 'yy-mm-dd',
            minDate: 'toDay()'
        }
    ).datepicker('setDate', now);
    console.log('here');
    $.ajax({
        url: "date_input",
        type: "POST",
        data : {date: now},
        dataType: "json",
        cache: false,
        success: function(ordered_table) {
            $('.list-table').removeClass('lock-table')
            jQuery.each(ordered_table, function(i, table) {
            id = table.fields.table;
            $('.list-table[data-item=' + id +']').addClass('lock-table')
            });
        },
        error: function (xhr, ajaxOptions, thrownError) {
            alert(xhr.status);
            alert(thrownError);
        }
    });
  datepicker.change(function (event) {
    var date = {
      'date': $(this).val()}
      $('#date').val($(this).val());
      $.ajax({
            url: "date_input",
            type: "POST",
            data : date,
            dataType: "json",
            cache: false,
            success: function(ordered_table) {
                  $('.list-table').removeClass('lock-table')
                  jQuery.each(ordered_table, function(i, table) {
                  id = table.fields.table;
                  $('.list-table[data-item=' + id +']').addClass('lock-table')
                  });
                },
            error: function (xhr, ajaxOptions, thrownError) {
                  alert(xhr.status);
                  alert(thrownError);
                }
            });
        return false;
    });
  $(function(){
    $('.list-table').click(function (event) {
      if (!$(this).hasClass('lock-table')){
        id = $(this).attr('data-item');
        $('#table_id').val(id);
        $(this).addClass('selected');
      };
    });
  });
    $('.list-table').click(function () {
      $('.list-table').removeClass('selected')
  });
  $(function(){
    $('.cancel').click(function(){
      $(".cancel-order").toggle();
    });
  });

  $(function(){
    $('.toast-item-close').click(function(){
      $(".toast-container").hide(500);
    });
  });
  $(function(){
    $('.list-table').click(function(){
      $(".table-help").hide(500);
    });
  });
});



var csrftoken = getCookie('csrftoken')