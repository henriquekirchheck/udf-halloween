{
  description = "Develop Python on Nix with uv";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs =
    { nixpkgs, flake-utils, ... }:
    flake-utils.lib.eachDefaultSystem (
      system:
      let
        inherit (nixpkgs) lib;
        pkgs = import nixpkgs { inherit system; };
      in
      {
        devShells = {
          default = pkgs.mkShell {
            nativeBuildInputs = with pkgs; [
              pkg-config
              uv
            ];

            buildInputs = with pkgs; [
              sdl3
              sdl2-compat
              SDL2_gfx
              SDL2_image
              SDL2_ttf
              SDL2_sound
              SDL2_mixer
              freetype
              portmidi
              python3
              xorg.libX11
            ];

            shellHook = ''
              unset PYTHONPATH
              uv sync
              . .venv/bin/activate
            '';
          };
        };
      }
    );
}
