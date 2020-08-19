$(document).ready(function(){
    $(".sidenav").sidenav({edge: "right"});
    $('.slider').slider({indicators: "true"});
    $('.scrollspy').scrollSpy();
    $('.fixed-action-btn').floatingActionButton();
    $('.modal').modal();
    $('.tooltipped').tooltip();
  });

  $('.carousel.carousel-slider').carousel({
    fullWidth: true,
    indicators: true
  });