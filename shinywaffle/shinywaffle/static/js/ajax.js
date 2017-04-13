/**
 * Created by alexandre on 10.04.2017.
 */


import * as tools from 'tools'


const ajaxHeaders = new Headers();

export const HTTPHandling = {
    200: success
};

export function HTTPDefault(response) {
    throw "200 expected, got " + response.status;
}

function success(response) {
    return response.json();
}


export default class Process {
    constructor(object, args = {}) {
        var p = this.m_preprocess;
        var s = this.m_success;
        var f = this.m_fail;

        var {
            preprocess = p,
            success = s,
            fail = f
            } = args;

        this.master = object;
        this.preprocess = preprocess;
        this.success = success;
        this.fail = fail;
    }

    m_preprocess() {
        tools.switchClass(this.master, 'available', 'deleting');
        this.master.find('*').addClass('disabled');
    }

    m_success(data) {
        this.master.slideUp();
    }

    m_fail(data, error, details) {
        console.log(data.responseText);
        console.log(data, error, details);
        tools.switchClass(this.master, 'deleting', 'delete-failed');
        window.setTimeout(() => tools.switchClass(this.master, 'delete-failed', 'available'), 1000);
        this.master.find('*').removeClass('disabled');
    }
}


export function driver(url, method, data) {
    var formData = new FormData();
    for(var k in data) {
        if (data.hasOwnProperty(k)) {
            formData.append(k, data[k])
        }
    }

    return fetch(url, {
        method: method,
        credentials: 'same-origin',
        body: formData,
        headers: ajaxHeaders
    });
}


export function setup() {
    ajaxHeaders.append('X-CSRFToken', tools.getCookie('csrftoken'))
}

//function csrfSafeMethod(method) {
//    // these HTTP methods do not require CSRF protection
//    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
//}
