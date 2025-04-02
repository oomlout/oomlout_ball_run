$fn = 50;


difference() {
	union() {
		translate(v = [15.0000000000, 0, 0]) {
			hull() {
				translate(v = [-9.5000000000, 17.0000000000, 0]) {
					cylinder(h = 6, r = 5);
				}
				translate(v = [9.5000000000, 17.0000000000, 0]) {
					cylinder(h = 6, r = 5);
				}
				translate(v = [-9.5000000000, -17.0000000000, 0]) {
					cylinder(h = 6, r = 5);
				}
				translate(v = [9.5000000000, -17.0000000000, 0]) {
					cylinder(h = 6, r = 5);
				}
			}
		}
	}
	union() {
		#translate(v = [7.5000000000, 0, 0]) {
			cylinder(h = 6, r = 1.8000000000);
		}
		translate(v = [0, 0, 5.5000000000]) {
			#rotate_extrude(angle = 360) {
				translate(v = [15.0000000000, 0, 0]) {
					circle(r = 1.6250000000);
				}
			}
		}
	}
}