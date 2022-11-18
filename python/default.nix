{ pkgs ? import <nixpkgs> { } }:
pkgs.mkShell {
  # nativeBuildInputs is usually what you want -- tools you need to run
  nativeBuildInputs = with pkgs; [
    exercism
    python310
    python310Packages.pytest
    python310Packages.pytest-cache
    python310Packages.pytest-subtests
    fish
  ];
}
