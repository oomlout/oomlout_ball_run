$fn = 50;


difference() {
	union() {
		hull() {
			translate(v = [-39.5000000000, 2.0000000000, 0]) {
				cylinder(h = 6, r = 5);
			}
			translate(v = [39.5000000000, 2.0000000000, 0]) {
				cylinder(h = 6, r = 5);
			}
			translate(v = [-39.5000000000, -2.0000000000, 0]) {
				cylinder(h = 6, r = 5);
			}
			translate(v = [39.5000000000, -2.0000000000, 0]) {
				cylinder(h = 6, r = 5);
			}
		}
		translate(v = [37.5000000000, 7.5000000000, 0]) {
			hull() {
				translate(v = [-2.0000000000, 9.5000000000, 0]) {
					cylinder(h = 6, r = 5);
				}
				translate(v = [2.0000000000, 9.5000000000, 0]) {
					cylinder(h = 6, r = 5);
				}
				translate(v = [-2.0000000000, -9.5000000000, 0]) {
					cylinder(h = 6, r = 5);
				}
				translate(v = [2.0000000000, -9.5000000000, 0]) {
					cylinder(h = 6, r = 5);
				}
			}
		}
		translate(v = [-37.5000000000, 7.5000000000, 0]) {
			hull() {
				translate(v = [-2.0000000000, 9.5000000000, 0]) {
					cylinder(h = 6, r = 5);
				}
				translate(v = [2.0000000000, 9.5000000000, 0]) {
					cylinder(h = 6, r = 5);
				}
				translate(v = [-2.0000000000, -9.5000000000, 0]) {
					cylinder(h = 6, r = 5);
				}
				translate(v = [2.0000000000, -9.5000000000, 0]) {
					cylinder(h = 6, r = 5);
				}
			}
		}
	}
	union() {
		#translate(v = [37.5000000000, 15, 0]) {
			cylinder(h = 6, r = 1.8000000000);
		}
		#translate(v = [-37.5000000000, 15, 0]) {
			cylinder(h = 6, r = 1.8000000000);
		}
		translate(v = [-45.0000000000, 0, 4.0000000000]) {
			rotate(a = [0, 90, 0]) {
				cylinder(h = 90, r = 3.2500000000);
			}
		}
	}
}