# Use the official Rust image as a base
FROM rust:sha256:d30c7ad62c2044e0d1174d742f0efbc02c1e43aea988193b6686ee8aaaf79170 AS build

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
FROM rust:sha256:d30c7ad62c2044e0d1174d742f0efbc02c1e43aea988193b6686ee8aaaf79170

# copy the build artifact from the build stage
COPY --from=build /task/target/release/task .

COPY start.sh  .

RUN  chmod +x start.sh

EXPOSE 3500
# set the startup command to run your binary

ENTRYPOINT "./start.sh"