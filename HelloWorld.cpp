"use strict";
 
var canvas;
var gl;
 
var points = [];
 
var NumTimesToSubdivide = 5;
 
window.onload = function init()
{
    canvas = document.getElementById( "gl-canvas" );
    gl = WebGLUtils.setupWebGL( canvas );
    if ( !gl ) { alert( "WebGL isn't available" ); }
 
    //
    //  Initialize our data for the Sierpinski Gasket
    //
 
    // First, initialize the corners of our gasket with three points.
 
    var vertices = [
        vec2( -1, -1 ),
        vec2(  0,  1 ),
        vec2(  1, -1 )
    ];
 
    divideTriangle( vertices[0], vertices[1], vertices[2],
                    NumTimesToSubdivide);
 
    //
    //  Configure WebGL
    //
    gl.viewport( 0, 0, canvas.width, canvas.height );
    gl.clearColor( 1.0, 1.0, 1.0, 1.0 );
 
    //  Load shaders and initialize attribute buffers
 
    var program = initShaders( gl, "vertex-shader", "fragment-shader" );
    gl.useProgram( program );
 
    // Load the data into the GPU
 
    var bufferId = gl.createBuffer();
    gl.bindBuffer( gl.ARRAY_BUFFER, bufferId );
    gl.bufferData( gl.ARRAY_BUFFER, flatten(points), gl.STATIC_DRAW );
 
    // Associate out shader variables with our data buffer
 
    var vPosition = gl.getAttribLocation( program, "vPosition" );
    gl.vertexAttribPointer( vPosition, 2, gl.FLOAT, false, 0, 0 );
    gl.enableVertexAttribArray( vPosition );
 
    render();
};
 
function triangle( a, b, c )
{
    points.push( a, b, c );
}
 
//----------------------------------------------------------------
function area(a, b, c)
{
    // assume a, b, and c are two-dimensional points
     return Math.abs(0.5 * (a[1] * b[0] - a[0] * b[1] +
                            b[1] * c[0] - b[0] * c[1] +
                            c[1] * a[0] - c[0] * a[1]));
}
//-----------------------------------------------------------------
function divideTriangle( a, b, c, count )
{
 
    // check for end of recursion
 
    if ( area(a,b,c) < 0.001 ) { // please god work
            // ^^ calls the area function to test if it is less than float 0.001, 
if not, it continues
            // to an else statement with an altered gokupoint to roate the 
triangles on each refresh
        triangle( a, b, c );
    }
    else {
 
        var gokupoint = Math.random() * 0.4 + 0.3;
        
        //bisect the sides
 
        var ab = mix( a, b, gokupoint );
        var ac = mix( a, c, gokupoint );
        var bc = mix( b, c, gokupoint );
 
        --count;
 
        // three new triangles
 
        divideTriangle( a, ab, ac, count );
        divideTriangle( c, ac, bc, count );
        divideTriangle( b, bc, ab, count );
    }
}
//-----------------------------------------------------
 
function render()
{
    gl.clear( gl.COLOR_BUFFER_BIT );
    gl.drawArrays( gl.TRIANGLES, 0, points.length );
}
