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



///////////////////////////////////////////
//////////////////TOOLS////////////////////
///////////////////////////////////////////

const urls = {
    deleteImage: '/galleries/images/delete/',
    deleteGallery: '/galleries/delete/'
};

var splitDelete = strip('_delete');
var splitUpdate = strip('_update');

function strip(pattern) {
    return function (id) {
        return id.split(pattern)[0];
    }
}


///////////////////////////////////////////
//////////////////INIT/////////////////////
///////////////////////////////////////////

$(function () {
    ajaxSetup();
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


///////////////////////////////////////////
//////////////////DELETE///////////////////
///////////////////////////////////////////

function deleteImage(event) {
    var url = urls.deleteImage;
    var id = splitDelete(event.target.id);
    deleteObject(id, url, function(data) {
        console.log('image deleted', data);
    })
}

function deleteGallery(event) {
    var url = urls.deleteGallery;
    var id = splitDelete(event.target.id);

    deleteObject(id, url, function(data) {
        console.log('gallery deleted', data);
    })
}

function deleteObject(id, url, success) {
    var method = 'POST';
    var data = {id: id};

    ajaxDriver(url, method, data)
        .done(success)
        .fail(function (data, error, status) {
            console.log(data.responseText, data, status);
        })
}



///////////////////////////////////////////
//////////////////AJAX/////////////////////
///////////////////////////////////////////

function ajaxDriver(url, method, data) {
    return $.ajax({
        url: url,
        type: method,
        data: data,
        dataType: 'json'
    })
}

function ajaxSetup() {
    var csrftoken = getCookie('csrftoken'); //Cookies.get('csrftoken');
    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

//temporary
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
