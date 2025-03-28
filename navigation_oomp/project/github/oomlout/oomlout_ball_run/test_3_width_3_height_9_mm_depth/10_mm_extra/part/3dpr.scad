$fn = 50;


difference() {
	union() {
		hull() {
			translate(v = [-17.0000000000, 17.0000000000, 0]) {
				cylinder(h = 9, r = 5);
			}
			translate(v = [17.0000000000, 17.0000000000, 0]) {
				cylinder(h = 9, r = 5);
			}
			translate(v = [-17.0000000000, -17.0000000000, 0]) {
				cylinder(h = 9, r = 5);
			}
			translate(v = [17.0000000000, -17.0000000000, 0]) {
				cylinder(h = 9, r = 5);
			}
		}
	}
	union() {
		#translate(v = [-15.0000000000, 22.5000000000, 0.0000000000]) {
			rotate(a = [90, 0, 0]) {
				cylinder(h = 45, r = 5);
			}
		}
		#translate(v = [-5.0000000000, 22.5000000000, 1.0000000000]) {
			rotate(a = [90, 0, 0]) {
				cylinder(h = 45, r = 5);
			}
		}
		#translate(v = [5.0000000000, 22.5000000000, 2.0000000000]) {
			rotate(a = [90, 0, 0]) {
				cylinder(h = 45, r = 5);
			}
		}
		#translate(v = [15.0000000000, 22.5000000000, 3.0000000000]) {
			rotate(a = [90, 0, 0]) {
				cylinder(h = 45, r = 5);
			}
		}
	}
}