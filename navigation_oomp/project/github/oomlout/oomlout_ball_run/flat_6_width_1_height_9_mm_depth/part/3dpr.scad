$fn = 50;


difference() {
	union() {
		hull() {
			translate(v = [-39.5000000000, 2.0000000000, 0]) {
				cylinder(h = 9, r = 5);
			}
			translate(v = [39.5000000000, 2.0000000000, 0]) {
				cylinder(h = 9, r = 5);
			}
			translate(v = [-39.5000000000, -2.0000000000, 0]) {
				cylinder(h = 9, r = 5);
			}
			translate(v = [39.5000000000, -2.0000000000, 0]) {
				cylinder(h = 9, r = 5);
			}
		}
	}
	union() {
		#translate(v = [-45.0000000000, 0, 8.0000000000]) {
			rotate(a = [0, 90, 0]) {
				cylinder(h = 90, r = 3.1750000000);
			}
		}
	}
}