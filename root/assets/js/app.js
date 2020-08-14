    $('.panel-collapse').on('show.bs.collapse', function () {
    $(this).siblings('.panel-heading').addClass('active');
        console.log("clicking");
  });

  $('.panel-collapse').on('hide.bs.collapse', function () {
      
        $(this).siblings('.panel-heading').removeClass('active');
  });