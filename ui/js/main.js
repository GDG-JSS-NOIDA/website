jQuery(function($) {
  "use strict", //Smooth scroll
    $(".navbar-collapse ul li a[href^='#']").on("click", function(e) {
    // prevent default anchor click behavior
    e.preventDefault();

    // store hash
    var hash = this.hash;

    // animate
    $("html, body").animate(
      {
        scrollTop: $(hash).offset().top //-1
      },
      300,
      function() {
        // when done, add hash to url
        // (default click behaviour)
        window.location.hash = hash;
      }
    );
  });

  $("#footer div a[href^='#']").on("click", function(e) {
    // prevent default anchor click behavior
    e.preventDefault();

    // store hash
    var hash = this.hash;

    // animate
    $("html, body").animate(
      {
        scrollTop: $(hash).offset().top
      },
      300,
      function() {
        // when done, add hash to url
        // (default click behaviour)
        window.location.hash = hash;
      }
    );
  });

  // portfolio filter
  $(window).load(function() {
    "use strict";
    var $portfolio_selectors = $(".portfolio-filter >li>a");
    var $portfolio = $(".portfolio-items");
    $portfolio.isotope({
      itemSelector: ".portfolio-item",
      layoutMode: "fitRows"
    });

    $portfolio_selectors.on("click", function() {
      $portfolio_selectors.removeClass("active");
      $(this).addClass("active");
      var selector = $(this).attr("data-filter");
      $portfolio.isotope({ filter: selector });
      return false;
    });
  });

  //Countdown js
  $("#countdown").countdown(
    {
      date: "10 july 2017 12:00:00",
      format: "on"
    },
    function() {
      // callback function
    }
  );
});
