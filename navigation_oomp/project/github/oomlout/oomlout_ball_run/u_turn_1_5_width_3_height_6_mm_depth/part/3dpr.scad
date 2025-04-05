$fn = 50;


difference() {
	union() {
		translate(v = [11.2500000000, 0, 0]) {
			hull() {
				translate(v = [-5.7500000000, 17.0000000000, 0]) {
					cylinder(h = 6, r = 5);
				}
				translate(v = [5.7500000000, 17.0000000000, 0]) {
					cylinder(h = 6, r = 5);
				}
				translate(v = [-5.7500000000, -17.0000000000, 0]) {
					cylinder(h = 6, r = 5);
				}
				translate(v = [5.7500000000, -17.0000000000, 0]) {
					cylinder(h = 6, r = 5);
				}
			}
		}
	}
	union() {
		#translate(v = [7.5000000000, 0, 0]) {
			cylinder(h = 6, r = 1.8000000000);
		}
		#translate(v = [15, 15, 0]) {
			cylinder(h = 6, r = 1.8000000000);
		}
		#translate(v = [15, -15, 0]) {
			cylinder(h = 6, r = 1.8000000000);
		}
		translate(v = [0, 0, 4.0000000000]) {
			#rotate_extrude(angle = 360) {
				translate(v = [16.7500000000, 0, 0]) {
					circle(r = 3.2500000000);
				}
			}
		}
	}
}