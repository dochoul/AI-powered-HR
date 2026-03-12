import { SearchIcon, SettingIcon, TrashIcon } from 'hiworks-icons/react/line/16';
import { O_Button, O_IconButton } from 'hiworks-ui-components';

function App() {
  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 24, padding: 24 }}>
      <div style={{ display: 'flex', gap: 8 }}>
        <O_Button variant="filled">filled</O_Button>
        <O_Button variant="outline">outline</O_Button>
        <O_Button variant="ghost">ghost</O_Button>
        <O_Button variant="text">text</O_Button>
        <O_Button variant="cancel">cancel</O_Button>
        <O_Button variant="destructive">destructive</O_Button>
        <O_Button variant="danger">danger</O_Button>
        <O_Button disabled>disabled</O_Button>
      </div>

      <div style={{ display: 'flex', gap: 8, alignItems: 'center' }}>
        <O_IconButton icon={<SettingIcon width="16px" height="16px" />} variant="filled" />
        <O_IconButton icon={<SettingIcon width="16px" height="16px" />} variant="outline" />
        <O_IconButton icon={<SettingIcon width="16px" height="16px" />} variant="ghost" />
        <O_IconButton icon={<SettingIcon width="16px" height="16px" />} variant="cancel" />
        <O_IconButton icon={<SettingIcon width="16px" height="16px" />} variant="destructive" />
        <O_IconButton icon={<SettingIcon width="16px" height="16px" />} variant="danger" />
        <O_IconButton icon={<SettingIcon width="16px" height="16px" />} disabled />
      </div>

      <div style={{ display: 'flex', gap: 8, alignItems: 'center' }}>
        <O_IconButton icon={<TrashIcon width="16px" height="16px" />} variant="destructive" />
        <O_IconButton icon={<SearchIcon width="16px" height="16px" />} variant="outline" />
      </div>
    </div>
  );
}

export default App;
