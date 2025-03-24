$(".alert > .btn-close").on('click', function() {
    $(this).closest(".alert").fadeOut('slow')
})