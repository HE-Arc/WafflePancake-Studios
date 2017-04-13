/**
 * Created by alexandre on 10.04.2017.
 */


import Process, * as ajax from 'ajax';


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

function getMaster(target, splitMethod) {
    var id = splitMethod(target) + '_master';
    return $('#' + id);
}



export function image(event) {
    var url = urls.deleteImage;
    deleteObject(event, url);
}

export function gallery(event) {
    var url = urls.deleteGallery;
    deleteObject(event, url);
}

function deleteObject(event, url) {
    var object = getMaster(event.target.id, splitDelete);
    var ajaxProcess = new Process(object, {disabled: [event.target]});
    var id = splitDelete(event.target.id);
    var data = {id: id};
    var method = 'POST';

    ajaxProcess.preprocess();

    ajax.driver(url, method, data)
        .then(response => {
            return ajax.HTTPHandling[response.status](response) || ajax.HTTPDefault(response);
        })
        .then(data => ajaxProcess.success(data))
        .catch((data, error, details) => ajaxProcess.fail(data, error, details))
}
