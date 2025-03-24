$('input[name="password"], #id_confirm_password').on('input', function() {

    const chars = Array.from($('input[name="password"]').val());

    const hasUppercase = chars.some(char => /[A-Z]/.test(char));
    const hasLowercase = chars.some(char => /[a-z]/.test(char));
    const hasSpecial = chars.some(char => /[!@#$%^*&():?]/.test(char));

    if(!hasLowercase) {
        $('div:has(> #id_confirm_password) > p:nth-of-type(3)').removeClass('text-muted').removeClass('text-success').addClass('text-danger')
    } else {
        $('div:has(> #id_confirm_password) > p:nth-of-type(3)').removeClass('text-muted').removeClass('text-danger').addClass('text-success')
    }

    if(!hasUppercase) {
        $('div:has(> #id_confirm_password) > p:nth-of-type(2)').removeClass('text-muted').removeClass('text-success').addClass('text-danger')
    } else {
        $('div:has(> #id_confirm_password) > p:nth-of-type(2)').removeClass('text-muted').removeClass('text-danger').addClass('text-success')
    }

    if(!hasSpecial) {
        $('div:has(> #id_confirm_password) > p:nth-of-type(4)').removeClass('text-muted').removeClass('text-success').addClass('text-danger')
    } else {
        $('div:has(> #id_confirm_password) > p:nth-of-type(4)').removeClass('text-muted').removeClass('text-danger').addClass('text-success')
    }

    if($('input[name="password"]').length > 8) {
        $('div:has(> #id_confirm_password) > p:nth-of-type(1)').removeClass('text-muted').removeClass('text-success').addClass('text-danger')
    } else {
        $('div:has(> #id_confirm_password) > p:nth-of-type(1)').removeClass('text-muted').removeClass('text-danger').addClass('text-success')
    }

    const confirm = $('#id_confirm_password')

    if(confirm.val() !== $('input[name="password"]').val()) {
        confirm.addClass('border border-danger')
    } else {
        confirm.removeClass('border border-danger')
    }
})