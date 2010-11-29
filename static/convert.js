function convert_address() {
    var address = $('#address').val()
    $.get('/convert/' + address,
        function (data) {
            $('#4lw').attr('href', 'http://' + data['4lw'])
            $('#4lw').html('http://' + data['4lw'])
        }
    )
}
