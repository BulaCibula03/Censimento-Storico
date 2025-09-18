# syntax=docker/dockerfile:1

ARG NODE_VERSION=20.19.2
FROM node:${NODE_VERSION}-alpine AS base

RUN apk add --no-cache python3 py3-pip

WORKDIR /usr/src/app
COPY requirements.txt .
RUN python3 -m venv /venv && /venv/bin/pip install --no-cache-dir -r requirements.txt

ENV PATH="/venv/bin:$PATH"

WORKDIR /usr/src/app

FROM base AS deps

RUN --mount=type=bind,source=package.json,target=package.json \
    --mount=type=bind,source=package-lock.json,target=package-lock.json \
    --mount=type=cache,target=/root/.npm \
    npm ci

FROM deps AS builder

COPY . .

RUN npm run build || echo "No build script"

FROM node:${NODE_VERSION}-alpine AS runtime

RUN apk add --no-cache python3 py3-pip

WORKDIR /usr/src/app

COPY --from=base /venv /venv
COPY --from=builder /usr/src/app /usr/src/app

ENV PATH="/venv/bin:$PATH"

EXPOSE 5000

CMD ["sh", "-c", "npm run dev"]