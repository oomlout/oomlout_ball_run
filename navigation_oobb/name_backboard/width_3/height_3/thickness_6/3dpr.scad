$fn = 50;


difference() {
	union() {
		translate(v = [-15.0000000000, -15.0000000000, 0]) {
			hull() {
				cylinder(h = 6, r = 5);
				cylinder(h = 6, r = 5);
				cylinder(h = 6, r = 5);
				cylinder(h = 6, r = 5);
			}
		}
		translate(v = [-15.0000000000, 0.0000000000, 0]) {
			hull() {
				cylinder(h = 6, r = 5);
				cylinder(h = 6, r = 5);
				cylinder(h = 6, r = 5);
				cylinder(h = 6, r = 5);
			}
		}
		translate(v = [-15.0000000000, 15.0000000000, 0]) {
			hull() {
				cylinder(h = 6, r = 5);
				cylinder(h = 6, r = 5);
				cylinder(h = 6, r = 5);
				cylinder(h = 6, r = 5);
			}
		}
		translate(v = [0.0000000000, -15.0000000000, 0]) {
			hull() {
				cylinder(h = 6, r = 5);
				cylinder(h = 6, r = 5);
				cylinder(h = 6, r = 5);
				cylinder(h = 6, r = 5);
			}
		}
		hull() {
			cylinder(h = 6, r = 5);
			cylinder(h = 6, r = 5);
			cylinder(h = 6, r = 5);
			cylinder(h = 6, r = 5);
		}
		translate(v = [0.0000000000, 15.0000000000, 0]) {
			hull() {
				cylinder(h = 6, r = 5);
				cylinder(h = 6, r = 5);
				cylinder(h = 6, r = 5);
				cylinder(h = 6, r = 5);
			}
		}
		translate(v = [15.0000000000, -15.0000000000, 0]) {
			hull() {
				cylinder(h = 6, r = 5);
				cylinder(h = 6, r = 5);
				cylinder(h = 6, r = 5);
				cylinder(h = 6, r = 5);
			}
		}
		translate(v = [15.0000000000, 0.0000000000, 0]) {
			hull() {
				cylinder(h = 6, r = 5);
				cylinder(h = 6, r = 5);
				cylinder(h = 6, r = 5);
				cylinder(h = 6, r = 5);
			}
		}
		translate(v = [15.0000000000, 15.0000000000, 0]) {
			hull() {
				cylinder(h = 6, r = 5);
				cylinder(h = 6, r = 5);
				cylinder(h = 6, r = 5);
				cylinder(h = 6, r = 5);
			}
		}
		translate(v = [0, -15.0000000000, 0]) {
			hull() {
				translate(v = [-20.0000000000, -0.5000000000, 0]) {
					cylinder(h = 3, r = 2);
				}
				translate(v = [20.0000000000, -0.5000000000, 0]) {
					cylinder(h = 3, r = 2);
				}
				translate(v = [-20.0000000000, 0.5000000000, 0]) {
					cylinder(h = 3, r = 2);
				}
				translate(v = [20.0000000000, 0.5000000000, 0]) {
					cylinder(h = 3, r = 2);
				}
			}
		}
		hull() {
			translate(v = [-20.0000000000, -0.5000000000, 0]) {
				cylinder(h = 3, r = 2);
			}
			translate(v = [20.0000000000, -0.5000000000, 0]) {
				cylinder(h = 3, r = 2);
			}
			translate(v = [-20.0000000000, 0.5000000000, 0]) {
				cylinder(h = 3, r = 2);
			}
			translate(v = [20.0000000000, 0.5000000000, 0]) {
				cylinder(h = 3, r = 2);
			}
		}
		translate(v = [0, 15.0000000000, 0]) {
			hull() {
				translate(v = [-20.0000000000, -0.5000000000, 0]) {
					cylinder(h = 3, r = 2);
				}
				translate(v = [20.0000000000, -0.5000000000, 0]) {
					cylinder(h = 3, r = 2);
				}
				translate(v = [-20.0000000000, 0.5000000000, 0]) {
					cylinder(h = 3, r = 2);
				}
				translate(v = [20.0000000000, 0.5000000000, 0]) {
					cylinder(h = 3, r = 2);
				}
			}
		}
		translate(v = [-15.0000000000, 0, 0]) {
			hull() {
				translate(v = [0.5000000000, 20.0000000000, 0]) {
					cylinder(h = 3, r = 2);
				}
				translate(v = [-0.5000000000, 20.0000000000, 0]) {
					cylinder(h = 3, r = 2);
				}
				translate(v = [0.5000000000, -20.0000000000, 0]) {
					cylinder(h = 3, r = 2);
				}
				translate(v = [-0.5000000000, -20.0000000000, 0]) {
					cylinder(h = 3, r = 2);
				}
			}
		}
		hull() {
			translate(v = [0.5000000000, 20.0000000000, 0]) {
				cylinder(h = 3, r = 2);
			}
			translate(v = [-0.5000000000, 20.0000000000, 0]) {
				cylinder(h = 3, r = 2);
			}
			translate(v = [0.5000000000, -20.0000000000, 0]) {
				cylinder(h = 3, r = 2);
			}
			translate(v = [-0.5000000000, -20.0000000000, 0]) {
				cylinder(h = 3, r = 2);
			}
		}
		translate(v = [15.0000000000, 0, 0]) {
			hull() {
				translate(v = [0.5000000000, 20.0000000000, 0]) {
					cylinder(h = 3, r = 2);
				}
				translate(v = [-0.5000000000, 20.0000000000, 0]) {
					cylinder(h = 3, r = 2);
				}
				translate(v = [0.5000000000, -20.0000000000, 0]) {
					cylinder(h = 3, r = 2);
				}
				translate(v = [-0.5000000000, -20.0000000000, 0]) {
					cylinder(h = 3, r = 2);
				}
			}
		}
	}
	union() {
		translate(v = [-15.0000000000, -15.0000000000, 0]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, -100.0000000000]) {
							cylinder(h = 200, r = 1.8000000000);
						}
						linear_extrude(height = 2.5000000000) {
							polygon(points = [[3.4620000000, 0.0000000000], [1.7310000000, 2.9981799479], [-1.7310000000, 2.9981799479], [-3.4620000000, 0.0000000000], [-1.7310000000, -2.9981799479], [1.7310000000, -2.9981799479]]);
						}
						translate(v = [0, 0, -100.0000000000]) {
							cylinder(h = 200, r = 1.8000000000);
						}
						translate(v = [0, 0, -100.0000000000]) {
							cylinder(h = 200, r = 1.8000000000);
						}
					}
					union();
				}
			}
		}
		translate(v = [-15.0000000000, 0.0000000000, 0]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, -100.0000000000]) {
							cylinder(h = 200, r = 1.8000000000);
						}
						linear_extrude(height = 2.5000000000) {
							polygon(points = [[3.4620000000, 0.0000000000], [1.7310000000, 2.9981799479], [-1.7310000000, 2.9981799479], [-3.4620000000, 0.0000000000], [-1.7310000000, -2.9981799479], [1.7310000000, -2.9981799479]]);
						}
						translate(v = [0, 0, -100.0000000000]) {
							cylinder(h = 200, r = 1.8000000000);
						}
						translate(v = [0, 0, -100.0000000000]) {
							cylinder(h = 200, r = 1.8000000000);
						}
					}
					union();
				}
			}
		}
		translate(v = [-15.0000000000, 15.0000000000, 0]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, -100.0000000000]) {
							cylinder(h = 200, r = 1.8000000000);
						}
						linear_extrude(height = 2.5000000000) {
							polygon(points = [[3.4620000000, 0.0000000000], [1.7310000000, 2.9981799479], [-1.7310000000, 2.9981799479], [-3.4620000000, 0.0000000000], [-1.7310000000, -2.9981799479], [1.7310000000, -2.9981799479]]);
						}
						translate(v = [0, 0, -100.0000000000]) {
							cylinder(h = 200, r = 1.8000000000);
						}
						translate(v = [0, 0, -100.0000000000]) {
							cylinder(h = 200, r = 1.8000000000);
						}
					}
					union();
				}
			}
		}
		translate(v = [0.0000000000, -15.0000000000, 0]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, -100.0000000000]) {
							cylinder(h = 200, r = 1.8000000000);
						}
						linear_extrude(height = 2.5000000000) {
							polygon(points = [[3.4620000000, 0.0000000000], [1.7310000000, 2.9981799479], [-1.7310000000, 2.9981799479], [-3.4620000000, 0.0000000000], [-1.7310000000, -2.9981799479], [1.7310000000, -2.9981799479]]);
						}
						translate(v = [0, 0, -100.0000000000]) {
							cylinder(h = 200, r = 1.8000000000);
						}
						translate(v = [0, 0, -100.0000000000]) {
							cylinder(h = 200, r = 1.8000000000);
						}
					}
					union();
				}
			}
		}
		translate(v = [0.0000000000, 0.0000000000, 0]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, -100.0000000000]) {
							cylinder(h = 200, r = 1.8000000000);
						}
						linear_extrude(height = 2.5000000000) {
							polygon(points = [[3.4620000000, 0.0000000000], [1.7310000000, 2.9981799479], [-1.7310000000, 2.9981799479], [-3.4620000000, 0.0000000000], [-1.7310000000, -2.9981799479], [1.7310000000, -2.9981799479]]);
						}
						translate(v = [0, 0, -100.0000000000]) {
							cylinder(h = 200, r = 1.8000000000);
						}
						translate(v = [0, 0, -100.0000000000]) {
							cylinder(h = 200, r = 1.8000000000);
						}
					}
					union();
				}
			}
		}
		translate(v = [0.0000000000, 15.0000000000, 0]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, -100.0000000000]) {
							cylinder(h = 200, r = 1.8000000000);
						}
						linear_extrude(height = 2.5000000000) {
							polygon(points = [[3.4620000000, 0.0000000000], [1.7310000000, 2.9981799479], [-1.7310000000, 2.9981799479], [-3.4620000000, 0.0000000000], [-1.7310000000, -2.9981799479], [1.7310000000, -2.9981799479]]);
						}
						translate(v = [0, 0, -100.0000000000]) {
							cylinder(h = 200, r = 1.8000000000);
						}
						translate(v = [0, 0, -100.0000000000]) {
							cylinder(h = 200, r = 1.8000000000);
						}
					}
					union();
				}
			}
		}
		translate(v = [15.0000000000, -15.0000000000, 0]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, -100.0000000000]) {
							cylinder(h = 200, r = 1.8000000000);
						}
						linear_extrude(height = 2.5000000000) {
							polygon(points = [[3.4620000000, 0.0000000000], [1.7310000000, 2.9981799479], [-1.7310000000, 2.9981799479], [-3.4620000000, 0.0000000000], [-1.7310000000, -2.9981799479], [1.7310000000, -2.9981799479]]);
						}
						translate(v = [0, 0, -100.0000000000]) {
							cylinder(h = 200, r = 1.8000000000);
						}
						translate(v = [0, 0, -100.0000000000]) {
							cylinder(h = 200, r = 1.8000000000);
						}
					}
					union();
				}
			}
		}
		translate(v = [15.0000000000, 0.0000000000, 0]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, -100.0000000000]) {
							cylinder(h = 200, r = 1.8000000000);
						}
						linear_extrude(height = 2.5000000000) {
							polygon(points = [[3.4620000000, 0.0000000000], [1.7310000000, 2.9981799479], [-1.7310000000, 2.9981799479], [-3.4620000000, 0.0000000000], [-1.7310000000, -2.9981799479], [1.7310000000, -2.9981799479]]);
						}
						translate(v = [0, 0, -100.0000000000]) {
							cylinder(h = 200, r = 1.8000000000);
						}
						translate(v = [0, 0, -100.0000000000]) {
							cylinder(h = 200, r = 1.8000000000);
						}
					}
					union();
				}
			}
		}
		translate(v = [15.0000000000, 15.0000000000, 0]) {
			rotate(a = [0, 0, 0]) {
				difference() {
					union() {
						translate(v = [0, 0, -100.0000000000]) {
							cylinder(h = 200, r = 1.8000000000);
						}
						linear_extrude(height = 2.5000000000) {
							polygon(points = [[3.4620000000, 0.0000000000], [1.7310000000, 2.9981799479], [-1.7310000000, 2.9981799479], [-3.4620000000, 0.0000000000], [-1.7310000000, -2.9981799479], [1.7310000000, -2.9981799479]]);
						}
						translate(v = [0, 0, -100.0000000000]) {
							cylinder(h = 200, r = 1.8000000000);
						}
						translate(v = [0, 0, -100.0000000000]) {
							cylinder(h = 200, r = 1.8000000000);
						}
					}
					union();
				}
			}
		}
	}
}