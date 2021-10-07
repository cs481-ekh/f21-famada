$(document).ready(function () {
  M.AutoInit();
  // $(".sidenav").sidenav();
  // $("select").formSelect();

  // search and view select columns logic for select all
  var select_all = $("#search-view-columns").find("li").eq("1");
  select_all.on("click", function () {
    if (select_all.hasClass("selected")) {
      $(this)
        .siblings()
        .not(".disabled")
        .each(function () {
          if (!$(this).hasClass("selected")) {
            $(this).click();
          }
        });
    }

    if (!select_all.hasClass("selected")) {
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
