$(function () {
    $('#paid_unpaid').hide();
    $('#billed_unbilled').hide();
    $('#type').change(function () {
        if ($('#type').val() == 'Caregiver Only') {
            $('#billed_unbilled').hide();
            $('#paid_unpaid').show();
        }
        else if ($('#type').val() == 'Client Only') {
            $('#paid_unpaid').hide();
            $('#billed_unbilled').show();
        } 
        else {
            $('#paid_unpaid').hide();
            $('#billed_unbilled').hide();
        }
    });

    $('#pay_hours').hide();
    $('#pay_select').change(function () {
        if ($('#pay_select').val() == 'Rounded') {
            $('#pay_hours').show();
        }
        else {
            $('#pay_hours').hide();
        }
    });
});
