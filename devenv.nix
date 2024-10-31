{ pkgs, lib, config, inputs, ... }:

{
  packages = with pkgs; [ 
    git
    stdenv.cc.cc
    zlib
    libGL
    libGLU
    SDL2
    xorg.libX11
  ];

  languages.python = {
    enable = true;
    package = pkgs.python312;
    poetry = {
      enable = true;
      activate.enable = true;
      install.enable = true;
    };
  };

  env = {
    LD_LIBRARY_PATH = "${pkgs.stdenv.cc.cc.lib}/lib:${pkgs.zlib}/lib:${pkgs.libGL}/lib:${pkgs.libGLU}/lib:${pkgs.SDL2}/lib";
  };

  devcontainer = {
    enable = true;
    settings = {
      customizations.vscode.extensions = [
        "mkhl.direnv"
        "jnoortheen.nix-ide"
        "ms-python.python"
        "tamasfe.even-better-toml"
      ];
    };
  };
}
