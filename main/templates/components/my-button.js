class MyButton extends HTMLElement {
    constructor() {
        super();
        this.text = '';
        this.color = '';
        this.url = '';
        this.render();
    }

    connectedVoidCallback() {
        this.text = this.getAttribute('text'),
        this.color = this.getAttribute('color'),
        this.url = this.getAttribute('url'),
        this.render()
    }

    render() {
        this.innerHTML.innerHTML = `
            <style>
                .button {
                    display: inline-block;
                    padding: 12px 24px;
                    border: none;
                    border-radius: 6px;
                    cursor: pointer;
                    text-align: center;
                    color: #e0e0e0;
                    text-decoration: none;
                    font-weight: 700;
                    font-size: 1rem;
                    transition: background-color 0.3s ease, transform 0.2s ease;
                    background-color: ${this.getColor(color)};
                }

                .button:hover {
                    background-color: #45456a;
                    transform: scale(1.05);
                }
            </style>
            <a href="${url}" target="_blank" class="button">${text}</a>
        `;
    }

    getColor(color) {
        const colors = {
            green: 'rgb(17, 187, 17)',
            orange: 'rgb(255, 94, 0)',
            blue: 'rgb(67, 164, 228)',
            red: 'rgb(199, 30, 55)',
            'dark-blue': 'rgb(14, 57, 198)'
        };
        return colors[color] || 'gray';
    }
}

customElements.define('my-button', MyButton);
