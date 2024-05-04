# Use the official Rust image as a base
FROM rust:latest AS build

RUN USER=root cargo new --bin task

WORKDIR /task

# Copy the Cargo.toml and Cargo.lock files to leverage Docker layer caching
COPY Cargo.toml Cargo.lock ./

# Build the application
RUN cargo build --release
RUN rm src/*.rs

COPY ./src ./src

RUN rm ./target/release/deps/task*
RUN cargo build --release

# our final base
FROM rust:latest

# copy the build artifact from the build stage
COPY --from=build /task/target/release/task .

COPY start.sh  .

RUN  chmod +x start.sh

EXPOSE 3500
# set the startup command to run your binary

ENTRYPOINT "./start.sh"