#version 150

in vec4 p3d_Vertex;
in vec2 p3d_MultiTexCoord0;
out vec2 v_texcoord;

void main() {
    gl_Position = p3d_Vertex;
    v_texcoord = p3d_MultiTexCoord0;
}
