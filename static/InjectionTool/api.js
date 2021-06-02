document.writeln("<link href=\'/pinglun/css/pinglun.css\' rel=\'stylesheet\' />");
document.writeln("<script src=\'/pinglun/js/pinglun.js\'></script>");

document.writeln("<div class=\"form-group mt-3\">");
document.writeln("    <textarea placeholder=\"留下您的精彩评论吧\" class=\"form-control\" id=\"txtCContent\" rows=\"3\"></textarea>");
document.writeln("</div>");
document.writeln("<div class=\"text-right\">");
document.writeln("  <button type=\"button\" class=\"btn btn-success\" id=\'btnCSumbit\' onclick=\'btnCSumbit_onclick();\'>提交</button>");
document.writeln("</div>");

document.writeln("<div id=\'divCDetail\'>");
document.writeln("</div>");
document.writeln("<div id=\'divCAddMore\'>");
document.writeln("<button type=\"button\"  class=\"btn btn-info\" id=\'btnCAddMore\' onclick=\"btnCAddMore_onclick();\" value=\"\">点击加载更多精彩评论</button>");
document.writeln("</div>");
document.writeln("<div id=\'divCNoMore\'>暂时没有更多评论</div>");