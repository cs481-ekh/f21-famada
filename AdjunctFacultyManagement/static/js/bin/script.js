$(document).ready(function () {
  M.AutoInit();
  // $(".sidenav").sidenav();
  // $("select").formSelect();

  // search and view select columns logic for select all
   $("select.grid-columns")
      .siblings("ul")
      .prepend(
        '<li id=sm_select_all class="select-all selected" ><span>Select all/none</span></li>'
      );

  var select_all = $("li.select-all")
  select_all.on("click", function () {
    if (select_all.hasClass("selected")) {
      $(this).removeClass('selected');
      $(this)
        .siblings()
        .not(".disabled")
        .each(function () {
          if (!$(this).hasClass("selected")) {
            $(this).click();
          }
        });
    }

    else if (!select_all.hasClass("selected")) {
      $(this).addClass('selected');
      $(this)
        .siblings()
        .not(".disabled")
        .each(function () {
          if ($(this).hasClass("selected")) {
            $(this).click();
          }
        });
    }
  });
});
