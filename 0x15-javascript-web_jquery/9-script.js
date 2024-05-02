dy(function(){
    $.ajax({
        url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
        type: 'GET',
        success: function(data) {
            $('#hello').text(data.hello);
        }
    });
});
