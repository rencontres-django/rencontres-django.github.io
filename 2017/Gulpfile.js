var gulp = require('gulp');
var gutil = require("gulp-util");
var sass = require('gulp-sass');

// Watching watching scss/html files
gulp.task('watch', ['sass'], function () {
    gulp.watch("./sass/*.scss", ['sass']);
    gulp.watch("./sass/*/*.scss", ['sass']);
});

gulp.task('sassbuild', function () {
    return gulp.src("source/sass/*.scss")
        .pipe(sass())
        .pipe(autoprefixer("last 2 versions", "> 1%", "Explorer 9", "Android 3"))
        .pipe(gulp.env.production ? csso() : gutil.noop())
        .pipe(gulp.dest("static/css"))
});
 

gulp.task('sass', function () {
    return gulp.src('./sass/*.scss')
        .pipe(sass({
            includePaths:['node_modules/foundation-sites/scss']
        }))
        .pipe(gulp.dest('./css'));
});


gulp.task('default', ['watch']);