$(document).ready(function(){
    $('.sidenav').sidenav();
    $('select').formSelect();



    var toastHTML = '<span>I am toast content</span><button class="btn-flat toast-action">Undo</button>';
    var notificationToast = M.toast({html: toastHTML, displayLength: "Infinity"});
    







  });