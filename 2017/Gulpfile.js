var gulp = require('gulp');
var gutil = require("gulp-util");
var sass = require('gulp-sass');
var plumber = require("gulp-plumber");
var autoprefixer = require("gulp-autoprefixer");
var csso = require("gulp-csso");


// Watching watching scss/html files
gulp.task('watch', ['sass'], function () {
    gulp.watch("./sass/*.scss", ['sass']);
});

gulp.task('sassbuild', function () {
    return gulp.src("./sass/*.scss")
        .pipe(sass({
            includePaths: ['node_modules/foundation-sites/scss']
        }))
        .pipe(autoprefixer("last 2 versions", "> 1%", "Explorer 9", "Android 3"))
        .pipe(gutil.env.prod ? csso() : gutil.noop())
        .pipe(gulp.dest("./css"))
});


gulp.task('sass', function () {
    return gulp.src('./sass/*.scss')
        .pipe(sass({
            includePaths: ['node_modules/foundation-sites/scss']
        }))
        .pipe(gulp.dest('./css'));
});


gulp.task('default', ['watch']);