# Poznote Cozy Themes

Two light-mode custom themes for [Poznote](https://github.com/timothepoznanski/Poznote):

- **The Hearth** — oat paper, walnut ink, and restrained cinnamon. More bookish than the built-in Sepia.
- **The Greenhouse** — warm cream, soft sage, and moss. Earthier and less lavender than the built-in Lavender.

Both are token-only CSS overrides using Poznote's documented `--pz-*` custom-property system. Tested against the token definitions in Poznote **6.151.0**. They are intended for Poznote's **Light** base theme.

## Install both as selectable themes

1. In Poznote, open **Settings → Admin Tools → Custom CSS path**.
2. Upload `hearth.css` and `greenhouse.css`. This stores the files; do not select one as the instance-wide CSS override if you want users to choose independently.
3. Open **Settings → Admin Tools → Theme list**.
4. Enable each uploaded CSS file as a theme and set its base to **Light**. Keep the built-in themes you want available and arrange the order.
5. Save. Each user can now cycle through the shared theme list; the selected theme remains their own choice.

To revert, choose a built-in theme from the theme switcher. An administrator can also remove either custom theme from the Theme list or delete its stored CSS file in Custom CSS path. Uploading/applying a custom CSS file as the global override is a separate setting and affects everyone.

## Files

- `hearth.css`
- `greenhouse.css`

## References

- [Poznote personalization and custom CSS documentation](https://github.com/timothepoznanski/Poznote#personalization)
- [Poznote CSS token guide](https://github.com/timothepoznanski/Poznote/blob/main/src/public/css/README.md)
- [Poznote design tokens](https://github.com/timothepoznanski/Poznote/blob/main/src/public/css/tokens.css)

## License

WTFPL. See [`LICENSE`](LICENSE).
