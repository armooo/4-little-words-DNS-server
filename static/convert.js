function convert_address() {
    var address = $('#address').val()
    $.get('/convert/' + address,
        function (data) {
            $('#4lw').val(data['4lw'])
        }
    )
}
