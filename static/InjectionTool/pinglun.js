var _c_content = "";
var _c_commentID = 0;
var _c_level = 1;
function btnCSumbit_onclick() {
    if (!c_submit_validate()) return;
    var nickName = "";
    _c_content = encodeURIComponent(_c_content);
    var url = location.href;
    $.ajax({
        type: "POST",
        contentType: "application/json",
        url: "/Pinglun/Lord.asmx/Add",
        data: "{url: \"" + url + "\",nickName:\"" + nickName + "\",content:\"" + _c_content + "\"}",
        dataType: "json",
        error: function (result) { AjaxErrorFun(result); },
        complete: function () { },
        success: function () { submit_ajax_successful(); }
    });
}
function submit_ajax_successful() {
    alert("提交成功，管理员审核中，感谢您的留言！");
    document.getElementById("txtCContent").value = "";
}
function c_submit_validate() {
    try {
        _c_content = document.getElementById("txtCContent").value;
        if (_c_content.length < 5) {
            throw "内容字数至少5个字，请多说一些吧！";
        }
        if (_c_content.length > 1000) {
            throw "内容字数太多，请分多次或简单一下吧。";
        }
        return true;
    }
    catch (err) {
        alert(err);
        return false;
    }
}
function renderTime(dateTime) {
    var date = new Date(parseInt(dateTime.replace("/Date(", "").replace(")/", ""), 10));
    var month = date.getMonth() + 1 < 10 ? "0" + (date.getMonth() + 1) : date.getMonth() + 1;
    var currentDate = date.getDate() < 10 ? "0" + date.getDate() : date.getDate();
    var hour = date.getHours() < 10 ? "0" + date.getHours() : date.getHours();
    var min = date.getMinutes() < 10 ? "0" + date.getMinutes() : date.getMinutes();
    var sec = date.getSeconds() < 10 ? "0" + date.getSeconds() : date.getSeconds();
    return date.getFullYear() + "-" + month + "-" + currentDate + " " + hour + ":" + min + ":" + sec;
}
function btnCAddMore_onclick() {
    var url = location.href;
    $.ajax({
        type: "POST",
        contentType: "application/json",
        url: "/Pinglun/Lord.asmx/GetMore",
        data: "{url: \"" + url + "\",pinglunID:" + _c_commentID + "}",
        dataType: "json",
        error: function (result) { AjaxErrorFun(result); },
        complete: function () { },
        success: function (result) { addmore_ajax_successful(result); }
    });
}
function addmore_ajax_successful(result) {
    var arr = result.d;
    if (arr.length < 10) {
        document.getElementById("divCAddMore").style.display = "none";
        document.getElementById("divCNoMore").style.display = "";
    }
    for (var i = 0; i < arr.length; i++) {
        var div = "";
        div += "<div class=\"div_c_box\">";
        div += "<div class=\"div_c_box_caption\">" +
            "<span class=\"div_c_box_level\">" + _c_level + "楼" + "</span>" +
            "<span class=\"div_c_box_nickname\">网友</span>" +
            "<span class=\"div_c_box_date\">" + renderTime(arr[i].CreateDate) + "</span>" +
            "</div>";
        div += "<div class=\"div_c_box_content\">" + arr[i].Content + "</div>";
        div += "</div>";
        document.getElementById("divCDetail").innerHTML += div;
        _c_level++;
    }
    if (arr.length > 0) {
        _c_commentID = arr[arr.length - 1].ID;
    }
}
window.onload = function () {
    var url = location.href;
    document.getElementById("divCDetail").innerHTML = "评论加载中...";
    document.getElementById("divCAddMore").style.display = "none";
    document.getElementById("divCNoMore").style.display = "none";
    $.ajax({
        type: "POST",
        contentType: "application/json",
        url: "/Pinglun/Lord.asmx/Get",
        data: "{url: \"" + url + "\"}",
        dataType: "json",
        error: function (result) { AjaxErrorFun(result); },
        complete: function () { },
        success: function (result) { onload_ajax_successful(result); }
    });
};
function onload_ajax_successful(result) {
    document.getElementById("divCDetail").innerHTML = "";
    var arr = result.d;
    if (arr.length == 0) {
        var day2 = new Date();
        var s2 = day2.getFullYear() + "-" + (day2.getMonth() + 1) + "-" + day2.getDate();
        var html = "";
        html += "<div class=\"div_c_box\">";
        html += "<div class=\"div_c_box_caption\">" +
            "<span class=\"div_c_box_level\">1楼" + "</span>" +
            "<span class=\"div_c_box_nickname\">网友</span>" +
            "<span class=\"div_c_box_date\">" + s2 + "</span>" +
            "</div>";
        html += "<div class=\"div_c_box_content\">内容超级棒！</div>";
        html += "</div>";
        document.getElementById("divCDetail").innerHTML += html;
    }
    else {
        for (var i = 0; i < arr.length; i++) {
            var div = "";
            div += "<div class=\"div_c_box\">";
            div += "<div class=\"div_c_box_caption\">" +
                "<span class=\"div_c_box_level\">" + _c_level + "楼" + "</span>" +
                "<span class=\"div_c_box_nickname\">网友</span>" +
                "<span class=\"div_c_box_date\">" + renderTime(arr[i].CreateDate) + "</span>" +
                "</div>";
            div += "<div class=\"div_c_box_content\">" + arr[i].Content + "</div>";
            div += "</div>";
            document.getElementById("divCDetail").innerHTML += div;
            _c_level++;
        }
        _c_commentID = arr[arr.length - 1].ID;
        if (arr.length == 10) {
            document.getElementById("divCAddMore").style.display = "";
        }
    }
}