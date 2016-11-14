var KOLEDAR = function () {
	    var wrap, label,
	            months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];

	    function init(newWrap) {
            wrap     = $(newWrap || "#calendar");
            label    = wrap.find("#label");
            wrap.find("#prev").bind("click.calendar", function () { premikanjePoMesecih(false); });
            wrap.find("#next").bind("click.calendar", function () { premikanjePoMesecih(true);  }); //hocemo naslednji mesec
            label.bind("click", function () { premikanjePoMesecih(null, new Date().getMonth(), new Date().getFullYear()); }); //nastavimo na zdajšnji mesec,leto
            label.click();
	    }

	    function premikanjePoMesecih(next, month, year) {
            var curr = label.text().trim().split(" "), calendar, tempYear =  parseInt(curr[1], 10);
            month = month || ((next) ? ( (curr[0] === "December") ? 0 : months.indexOf(curr[0]) + 1 ) : ( (curr[0] === "January") ? 11 : months.indexOf(curr[0]) - 1 ));
            year = year || ((next && month === 0) ? tempYear + 1 : (
	    }

	    function createCalendar(year, month) {

	    }
	    createCalendar.cache = {};
	    return {
	        init : init,
	        switchMonth : switchMonth,
	        createCal   : createCal
	    };






