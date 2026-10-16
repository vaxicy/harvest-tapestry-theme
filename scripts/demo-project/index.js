// Harvest Tapestry Theme — slate ink, sage, cream paper and pressed-flower pink
import { readFile } from 'node:fs/promises';

const TAPESTRY_PALETTE = {
  slate: '#B8C3D3',
  sage: '#CEDABF',
  petal: '#E1C1D0',
  peach: '#EFD1CD',
  cream: '#FDECCE',
};

export class HarvestTapestry {
  constructor(name = 'Harvest moon') {
    this.name = name;
    this.colors = Object.values(TAPESTRY_PALETTE);
  }

  /** Blend two colors into a soft woven shade. */
  blend(from, to, ratio = 0.5) {
    const parse = (hex) => [1, 3, 5].map((i) => parseInt(hex.slice(i, i + 2), 16));
    const [a, b] = [parse(from), parse(to)];
    const channels = a.map((value, i) => Math.round(value * (1 - ratio) + b[i] * ratio));
    return '#' + channels.map((value) => value.toString(16).padStart(2, '0')).join('');
  }

  async describe(file) {
    const content = await readFile(file, 'utf8');
    return { name: this.name, colors: this.colors, content };
  }
}

const weave = new HarvestTapestry();
console.log(weave.blend(TAPESTRY_PALETTE.slate, TAPESTRY_PALETTE.cream));
