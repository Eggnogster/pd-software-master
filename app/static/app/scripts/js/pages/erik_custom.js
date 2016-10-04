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

    $('#co_billing').hide();
    $('#insurance').hide();
    $('#bill_method').change(function () {
        if ($('#bill_method').val() == '1') {
            $('#co_billing').hide();
            $('#insurance').hide();
            $('#self_pay').show();
        }
        else if ($('#bill_method').val() == '2') {
            $('#self_pay').hide();
            $('#insurance').hide();
            $('#co_billing').show();
        }
        else if ($('#bill_method').val() == '3') {
            $('#self_pay').hide();
            $('#co_billing').hide();
            $('#insurance').show();
        }
        else {
            $('#co_billing').hide();
            $('#insurance').hide();
        }
    });
});
