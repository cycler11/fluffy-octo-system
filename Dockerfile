FROM rust:1.82-slim

RUN apt-get update && apt-get install -y \
    pkg-config libpq-dev build-essential curl

WORKDIR /usr/src/app

COPY Cargo.toml Cargo.lock ./
RUN mkdir src && echo "fn main() {}" > src/main.rs
RUN cargo build --release
RUN rm -rf src

COPY . .

CMD ["cargo", "run", "--release"]
