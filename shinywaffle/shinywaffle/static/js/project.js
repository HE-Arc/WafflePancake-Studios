/* Project specific Javascript goes here. */

/*
Formatting hack to get around crispy-forms unfortunate hardcoding
in helpers.FormHelper:

    if template_pack == 'bootstrap4':
        grid_colum_matcher = re.compile('\w*col-(xs|sm|md|lg|xl)-\d+\w*')
        using_grid_layout = (grid_colum_matcher.match(self.label_class) or
                             grid_colum_matcher.match(self.field_class))
        if using_grid_layout:
            items['using_grid_layout'] = True

Issues with the above approach:

1. Fragile: Assumes Bootstrap 4's API doesn't change (it does)
2. Unforgiving: Doesn't allow for any variation in template design
3. Really Unforgiving: No way to override this behavior
4. Undocumented: No mention in the documentation, or it's too hard for me to find
*/
$('.form-group').removeClass('row');


///////////////////////////////////////////
///////////////////////////////////////////
///////////////////////////////////////////



var splitDelete = strip('_delete');
var splitUpdate = strip('_update');



$(function(){
    addEventListeners();
});

function addEventListeners() {
    $('body')
        .on('click', '.delete-button-image', deleteImage)
        .on('click', '.delete-button-gallery', deleteGallery)
        .on('click', '.delegate', closestClick)
}

function closestClick(event) {
    event.target.closest('.btn').click();
    event.stopPropagation();
}

function deleteImage(event) {
    var id = splitDelete(event.target.id);
    console.log(id);
}

function deleteGallery(event) {
    var url = '/galleries/delete/';
    var method = 'DELETE';
    var id = splitDelete(event.target.id);
    var data = {id: id};

    ajaxDriver(url, method, data)
        .done(function(data){
            console.log('win', data);
        })
        .fail(function(data, error, status) {
            console.log('fail', data, status);
        })
}

function strip(pattern) {
    return function(id) {
        return id.split(pattern)[0];
    }
}


function ajaxDriver(url, method, data) {
    return $.ajax({
        url: url,
        type: method,
        data: data,
        dataType: 'json'
    })
}
